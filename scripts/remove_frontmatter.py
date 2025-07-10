#!/usr/bin/env python3
"""Remove frontmatter and attribution from markdown files"""

import re
from pathlib import Path

def remove_frontmatter_and_attribution(file_path):
    """Remove YAML frontmatter and attribution blocks from a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove YAML frontmatter (everything between --- markers at the start)
    frontmatter_pattern = r'^---\n.*?\n---\n\n?'
    content = re.sub(frontmatter_pattern, '', content, flags=re.DOTALL)
    
    # Remove attribution info boxes
    attribution_pattern = r'!!! info "Source"\n(?:    .*\n)*\n?'
    content = re.sub(attribution_pattern, '', content, flags=re.MULTILINE)
    
    # Remove any leading blank lines
    content = content.lstrip('\n')
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# List of files that have sync tags
files_to_process = [
    '/workspace/docs/workflows/robotic-ultrasound-simulation.md',
    '/workspace/docs/workflows/robotic-ultrasound-quick-start.md',
    '/workspace/docs/workflows/robotic-ultrasound-dds-communication.md',
    '/workspace/docs/workflows/robotic-surgery-surgical-tasks.md',
    '/workspace/docs/workflows/robotic-surgery-quick-start.md',
    '/workspace/docs/sensor-simulation/ultrasound-raytracing.md',
    '/workspace/docs/workflows/tutorials/bring-your-own-xr.md',
    '/workspace/docs/workflows/tutorials/bring-your-own-patient.md',
    '/workspace/docs/workflows/robotic-ultrasound-train-pi-zero.md',
    '/workspace/docs/workflows/robotic-ultrasound-train-gr00t.md',
    '/workspace/docs/workflows/tutorials/mira-teleoperation.md',
    '/workspace/docs/workflows/telesurgery-quick-start.md',
    '/workspace/docs/workflows/robotic-ultrasound-visualization-tools.md',
    '/workspace/docs/workflows/robotic-ultrasound-policy-runner.md',
    '/workspace/docs/workflows/robotic-ultrasound-holoscan-apps.md',
]

# Process each file
for file_path in files_to_process:
    try:
        if remove_frontmatter_and_attribution(file_path):
            print(f"✓ Processed: {file_path}")
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")

print("\nDone! All frontmatter and attribution tags have been removed.")