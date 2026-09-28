import math

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy
from px4_msgs.msg import VehicleAttitude, VehicleLocalPosition, VehicleStatus


class TelemetryNode(Node):
    def __init__(self):
        super().__init__('px4_telemetry')
        self.declare_parameter('display_rate', 1.0)
        rate = float(self.get_parameter('display_rate').value)
        if rate <= 0:
            raise ValueError('display_rate must be positive')
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
        )
        self.attitude = None
        self.position = None
        self.status = None
        self.create_subscription(VehicleAttitude, '/fmu/out/vehicle_attitude', self.on_attitude, qos)
        self.create_subscription(VehicleLocalPosition, '/fmu/out/vehicle_local_position', self.on_position, qos)
        self.create_subscription(VehicleStatus, '/fmu/out/vehicle_status', self.on_status, qos)
        self.create_timer(1.0 / rate, self.display)

    def on_attitude(self, msg):
        self.attitude = msg

    def on_position(self, msg):
        self.position = msg

    def on_status(self, msg):
        self.status = msg

    @staticmethod
    def euler_degrees(q):
        w, x, y, z = q
        roll = math.atan2(2 * (w*x + y*z), 1 - 2 * (x*x + y*y))
        pitch = math.asin(max(-1.0, min(1.0, 2 * (w*y - z*x))))
        yaw = math.atan2(2 * (w*z + x*y), 1 - 2 * (y*y + z*z))
        return tuple(math.degrees(a) for a in (roll, pitch, yaw))

    def display(self):
        lines = ['PX4 telemetry (local NED / body FRD)']
        if self.attitude is not None:
            r, p, y = self.euler_degrees(self.attitude.q)
            lines.append(f'Attitude [deg]: roll={r:.2f}, pitch={p:.2f}, yaw={y:.2f}')
        else:
            lines.append('Attitude: waiting for data')
        if self.position is not None:
            pos = self.position
            if pos.xy_valid and pos.z_valid:
                lines.append(f'Position NED [m]: N={pos.x:.2f}, E={pos.y:.2f}, D={pos.z:.2f}')
            else:
                lines.append('Position: estimate not valid')
            if pos.v_xy_valid and pos.v_z_valid:
                lines.append(f'Velocity NED [m/s]: N={pos.vx:.2f}, E={pos.vy:.2f}, D={pos.vz:.2f}')
            else:
                lines.append('Velocity: estimate not valid')
        else:
            lines.append('Position/velocity: waiting for data')
        if self.status is not None:
            lines.append(f'Status: arming_state={self.status.arming_state}, nav_state={self.status.nav_state}')
        else:
            lines.append('Status: waiting for data')
        self.get_logger().info('\n' + '\n'.join(lines))


def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = TelemetryNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
