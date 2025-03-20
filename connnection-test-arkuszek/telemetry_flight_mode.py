#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def print_flight_mode():
    drone = System(mavsdk_server_address='localhost')
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break
    # async for flight_mode in drone.telemetry.flight_mode():
    #     print("FlightMode:", flight_mode)
    # async for altitude in drone.telemetry.altitude():
    #     print("Altittude:", altitude.altitude_local_m)

    async for position in drone.telemetry.position():
        print(f"Lat:{position.latitude_deg} || Lon:{position.longitude_deg}")

if __name__ == "__main__":
    # Start the main function
    asyncio.run(print_flight_mode())
