# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device x2
%define vendor leeco

%define vendor_pretty LeEco
%define device_pretty Le Max2

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 3.5

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc
