# Vehicle Details Retrieval Agent

[![Fetch.ai](https://img.shields.io/badge/Fetch.ai-uAgents-purple)](https://fetch.ai)
[![Agentverse](https://img.shields.io/badge/Agentverse-DeltaV-blue)](https://agentverse.ai)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://python.org)
[![RapidAPI](https://img.shields.io/badge/RapidAPI-Integrated-0055DA)](https://rapidapi.com)

An advanced vehicle details retrieval system built with Fetch.ai uAgents that provides comprehensive information about any Indian vehicle based on its registration number — including owner details, registration data, and outstanding traffic challans.

## Features

- **Vehicle Registration Lookup** — Retrieve owner name, registration date, vehicle class, fuel type, and more
- **Challan Detection** — Check for outstanding traffic violations and pending fines
- **DeltaV Integration** — Deployable to Agentverse for natural language queries via DeltaV
- **RTO API Integration** — Real-time data from the RTO Vehicle Information Verification API
- **Agent Protocol** — Publishes manifest for agent-to-agent discovery and communication

## How It Works

```
User Query (reg. number) → uAgent → RTO Vehicle API (RapidAPI) → Vehicle Details Response
```

1. User sends a vehicle registration number (e.g., "MH12AB1234")
2. The agent queries the RTO Vehicle Information API via RapidAPI
3. Returns comprehensive vehicle details including owner info, registration status, and challans
4. Responds via the uAgents protocol with formatted results

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | Fetch.ai uAgents |
| AI Engine | Fetch.ai AI Engine / DeltaV |
| Vehicle Data | RTO Vehicle Info Verification API (RapidAPI) |
| Data Models | Pydantic |

## Getting Started

### Prerequisites

- Python 3.8+
- RapidAPI key with access to the RTO Vehicle Information API

### Installation

```bash
git clone https://github.com/gautammanak1/Vehicle-Details-Retrieval.git
cd Vehicle-Details-Retrieval
pip install uagents requests pydantic ai-engine
```

### Configuration

Update the `rapidapi_key` variable in `vehicleAgent.py`:

```python
rapidapi_key = "your_rapidapi_key_here"
```

### Run

```bash
python vehicleAgent.py
```

### Deploy to Agentverse

The agent publishes its manifest on startup, making it discoverable on [Agentverse](https://agentverse.ai) and queryable through DeltaV.

## Project Structure

```
├── vehicleAgent.py      # Agent definition, API integration, message handling
├── private_keys.json    # Agent private keys (do not commit to public repos)
└── README.md
```

## API Response Example

```json
{
  "owner_name": "John Doe",
  "vehicle_class": "Motor Car",
  "fuel_type": "Petrol",
  "registration_date": "2020-01-15",
  "insurance_validity": "2025-01-15",
  "fitness_upto": "2035-01-14",
  "pending_challans": 0
}
```

## License

MIT
