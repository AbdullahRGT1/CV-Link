#!/usr/bin/env python3
"""Send OSC float commands to the Unreal Engine Bp_test Blueprint.

Get OSC Message Float At Index expects a float argument at Index 0.
Set TARGET_IP, TARGET_PORT and OSC_ADDRESS to match Bp_test.
"""

import socket
import struct
import sys

# Match these three values to the Create OSC Server setup in Bp_test.
TARGET_IP = "192.168.1.2"  # Use the Unreal PC's LAN IPv4 address from another device.
TARGET_PORT = 8080        # Must equal the port configured in Bp_test.
OSC_ADDRESS = "/test"    # Must equal any address filter configured in Bp_test.

PRESETS = {
    "stop": 0.0,
    "bus": 1.0,
    "airplane": 2.0,
    "boat": 3.0,
    "car": 4.0,
}


def osc_string(value: str) -> bytes:
    """Encode an OSC string with NUL termination and four-byte padding."""
    data = value.encode("utf-8") + b"\0"
    return data + b"\0" * ((-len(data)) % 4)


def make_osc_float_message(address: str, value: float) -> bytes:
    """Build one OSC message containing a single float32 argument."""
    if not address.startswith("/"):
        raise ValueError("OSC address must begin with '/'")
    return osc_string(address) + osc_string(",f") + struct.pack(">f", value)


def main() -> int:
    destination = (TARGET_IP, TARGET_PORT)
    print(f"OSC destination: {TARGET_IP}:{TARGET_PORT}  address: {OSC_ADDRESS}")
    print("Float argument index in Blueprint: 0")
    print("Commands: bus, airplane, boat, car, stop; a number; or q to quit.")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            while True:
                command = input("Command> ").strip().lower()
                if command in {"q", "quit", "exit"}:
                    break
                if not command:
                    continue

                try:
                    value = PRESETS[command] if command in PRESETS else float(command)
                    packet = make_osc_float_message(OSC_ADDRESS, value)
                except (ValueError, OverflowError) as exc:
                    print(f"Invalid command/value: {exc}")
                    continue

                sock.sendto(packet, destination)
                print(f"Sent float {value:g}")

            # Send stop on normal exit; Blueprint should map 0.0 to stop.
            sock.sendto(make_osc_float_message(OSC_ADDRESS, 0.0), destination)
            print("Sent stop value 0.0.")
    except (KeyboardInterrupt, EOFError):
        print("\nSender stopped.")
    except OSError as exc:
        print(f"UDP socket error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


