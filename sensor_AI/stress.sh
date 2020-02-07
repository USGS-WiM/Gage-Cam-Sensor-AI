#show CPU freq & Temp
echo "This is a Raspberry Pi 3b"
echo "Freq:"
cat  /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
echo "Temp:"
vcgencmd measure_temp
echo "Supplied Voltage:"
/opt/vc/bin/vcgencmd get_throttled


