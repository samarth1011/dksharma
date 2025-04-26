#!/usr/bin/bash

# Replace {YOUR_PROJECT_MAIN_DIR_NAME} with your actual project directory name
PROJECT_MAIN_DIR_NAME="dksharma"

sudo cp "/home/ec2-user/$PROJECT_MAIN_DIR_NAME/gunicorn/gunicorn_dksharma.socket" "/etc/systemd/system/gunicorn_dksharma.socket"
sudo cp "/home/ec2-user/$PROJECT_MAIN_DIR_NAME/gunicorn/gunicorn_dksharma.service" "/etc/systemd/system/gunicorn_dksharma.service"
# Start and enable Gunicorn service
sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
