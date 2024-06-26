import requests
from pydantic import Field
from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType

# Create an instance of VehicleProtocol
vehicle_protocol = Protocol(name="vehicle_protocol")

class VehicleDetailsRequest(Model):
    vehicle_number: str = Field(description="Vehicle number to fetch details")

class VehicleDetailsResponse(Model):
    details: dict = Field(description="Fetched vehicle details")

# Function to get vehicle details from the API
async def get_vehicle_details(vehicle_number, rapidapi_key):
    url = "https://rto-vehicle-information-verification-india.p.rapidapi.com/api/v1/rc/vehicleinfo"
    payload = {
        "reg_no": vehicle_number,
        "consent": "Y",
        "consent_text": "I hereby declare my consent agreement for fetching my information via AITAN Labs API"
    }
    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': rapidapi_key,
        'X-RapidAPI-Host': "rto-vehicle-information-verification-india.p.rapidapi.com"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

# Hardcoded RapidAPI key
rapidapi_key = ""  # Replace with your actual RapidAPI key be36d48f25msh2cae51229981e29p1d0cc1jsn5e058b8dbb93

@vehicle_protocol.on_message(model=VehicleDetailsRequest)
async def request_vehicle_details(ctx: Context, sender: str, msg: VehicleDetailsRequest):
    ctx.logger.info(f"Received vehicle details request from {sender}")
    details = await get_vehicle_details(msg.vehicle_number, rapidapi_key)
    
    await ctx.send(sender, VehicleDetailsResponse(details=details))
    ctx.logger.info(f"Sent vehicle details to {sender}")

    await ctx.send(sender, UAgentResponse(message="Vehicle details fetched successfully", type=UAgentResponseType.FINAL))

# Create and run the agent
if __name__ == "__main__":
    agent = Agent("vehicle_agent")
    agent.include(vehicle_protocol, publish_manifest=True)
    agent.run()
