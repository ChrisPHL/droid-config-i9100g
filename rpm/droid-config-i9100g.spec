# These and other macros are documented in ../droid-configs-device/droid-configs.inc
%define device i9100g
%define vendor samsung
%define vendor_pretty Samsung
%define device_pretty Galaxy S2 G
%define dcd_path ./
#Adjust this for your device (http://piratepad.net/hadk-faq) SGS2: 480x800 --> 480/540 = 0.8888
%define pixel_ratio 0.89
# We assume most devices will
%define have_modem 1
%include droid-configs-device/droid-configs.inc
