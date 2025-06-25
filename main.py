from my_agents.doctors import general_physician,ENT_Specialist,Physchatrist
from agents import Runner
import asyncio

print("Doctors choice you need to consult...")
async def main():
        result1 = await Runner.run (general_physician,"fever and flue")
        print("General Physician:", result1.final_output)
    
        result2 = await Runner.run (ENT_Specialist,"throat infection")
        print("ENT Specialist:", result2.final_output)
    
        result3 = await Runner.run (Physchatrist,"depression")
        print("Phychatrist:", result3.final_output)

asyncio.run(main())




