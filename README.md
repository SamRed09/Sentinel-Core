# 🛡️ SENTINEL: Automated Compliance & Audit System

**Sentinel** is a real-time cybersecurity auditing engine designed to enforce **NCA-ECC (National Cybersecurity Authority)** compliance across hybrid networks.

![System Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-blue)
![Tech Stack](https://img.shields.io/badge/Stack-Python%20%7C%20PostgreSQL%20%7C%20Grafana-orange)

## 🚀 Architecture
Sentinel operates on a **Client-Server** model:
1.  **The Core (Backend):** A PostgreSQL database stores audit logs in real-time.
2.  **The Agent (Python):** Lightweight scripts deploy to target nodes (Windows/Linux) to verify firewall, SSH, and patch status.
3.  **The Dashboard (Grafana):** A centralized SOC view for visualization and alerting.

## ⚡ Quick Start
### 1. Prerequisites
* Ubuntu 22.04 LTS (Recommended for Server)
* Python 3.10+
* PostgreSQL 14+
* Grafana 9+

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/SamRed09/Sentinel-Core.git](https://github.com/SamRed09/Sentinel-Core.git)

# Install dependencies
pip install psycopg2-binary
