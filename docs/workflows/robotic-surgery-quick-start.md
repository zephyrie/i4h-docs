# Robotic Surgery Workflow

![Robotic Surgery Workflow](../../assets/images/robotic_surgery_workflow.jpg)

The Robotic Surgery Workflow is a comprehensive solution designed for healthcare professionals and researchers working in the field of robotic-assisted surgery. This workflow provides a robust framework for simulating, training, and analyzing robotic surgical procedures in a virtual environment. It leverages NVIDIA's ray tracing capabilities to create highly realistic surgical simulations, enabling surgeons to practice complex procedures, researchers to develop new surgical techniques, and medical institutions to enhance their training programs. By offering a safe, controlled environment for surgical practice and research, this workflow helps improve surgical outcomes, reduce training costs, and advance the field of robotic surgery.


## Table of Contents
- [System Requirements](#system-requirements)
- [Environment Setup](#environment-setup)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
  - [Asset Setup](#asset-setup)
  - [Environment Variables](#environment-variables)
- [Running the Workflow](#running-the-workflow)

## System Requirements

### Hardware Requirements
- Ubuntu 22.04
- NVIDIA GPU with ray tracing capability
    - GPUs without RT Cores (A100, H100) are not supported
    - Minimum 8GB VRAM recommended
- 50GB of disk space
- 16GB RAM minimum

### Software Requirements
- [NVIDIA Driver Version >= 555](https://www.nvidia.com/en-us/drivers/)
- Python 3.10

## Environment Setup

**Note**: The setup process takes approximately 30-40 minutes to complete, depending on your system and network connection.

### Prerequisites

The robotic surgery workflow is built on the following dependencies:
- [IsaacSim 4.5.0](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/index.html)
- [IsaacLab 2.1.0](https://isaac-sim.github.io/IsaacLab/v2.1.0/index.html)

### Installation Steps

#### 1. Install NVIDIA Driver
Install or upgrade to the latest NVIDIA driver from [NVIDIA website](https://www.nvidia.com/en-us/drivers/)

**Note**: The workflow requires driver version >= 555 for ray tracing capabilities.

#### 2. Install Dependencies

##### Install Conda

[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) is recommended.

##### Create Conda Environment

```bash
# Create a new conda environment
conda create -n robotic_surgery python=3.10 -y
# Activate the environment
conda activate robotic_surgery
```

##### Clone repository
   ```bash
   git clone https://github.com/isaac-for-healthcare/i4h-workflows.git
   cd i4h-workflows
   ```

##### Install All Dependencies
The main script `tools/env_setup_robot_surgery.sh` installs all necessary dependencies:

###### Base Components
- IsaacSim 4.5.0 (and core dependencies)
- IsaacLab 2.1.0
- Essential build tools and libraries

Run the script from the repository root:
```bash
cd <path-to-i4h-workflows>
bash tools/env_setup_robot_surgery.sh
```

### Asset Setup

**Note**: The assets can be automatically retrieved when running the workflows. Optionally, you can also download all the assets in advance. Please note that the assets are approximately 65 GB and may take some time to download depending on your internet connection.

Download the required assets using:
```bash
i4h-asset-retrieve
```

This will download assets to `~/.cache/i4h-assets/<sha256>`. For more details, refer to the [Asset Container Helper](https://github.com/isaac-for-healthcare/i4h-asset-catalog/blob/main/docs/catalog_helper.md).

### Environment Variables

Before running any scripts, you need to set up the following environment variables:

1. **PYTHONPATH**: Set this to point to the scripts directory:
   ```bash
   export PYTHONPATH=<path-to-i4h-workflows>/workflows/robotic_surgery/scripts
   ```
   This ensures Python can find the modules under the [`scripts`](./scripts) directory.

## Running the Workflow

The robotic surgery workflow provides several example scripts demonstrating different components:

- [Simulation](./scripts/simulation)
  - Basic robot control
  - Surgical task simulation
  - State machine demonstrations
  - Reinforcement learning examples
