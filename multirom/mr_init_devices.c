#include <stdlib.h>

// These are paths to folders in /sys which contain "uevent" file
// need to init this device.
// MultiROM needs to init framebuffer, mmc blocks, input devices,
// some ADB-related stuff and USB drives, if OTG is supported
// You can use * at the end to init this folder and all its subfolders
const char *mr_init_devices[] =
{
    "/sys/devices/virtual/mem/null",
    "/sys/devices/virtual/misc/fuse",
    "/sys/class/graphics/fb0",

    "/sys/block/mmcblk0",
    "/sys/block/mmcblk0rpmb",
    "/sys/devices/soc.0/f9824900.sdhci",
    "/sys/devices/soc.0/f9824900.sdhci/mmc_host/mmc0",
    "/sys/devices/soc.0/f9824900.sdhci/mmc_host/mmc0/mmc0:0001",
    "/sys/devices/soc.0/f9824900.sdhci/mmc_host/mmc0/mmc0:0001/block/mmcblk0",
    "/sys/devices/soc.0/f9824900.sdhci/mmc_host/mmc0/mmc0:0001/block/mmcblk0/mmcblk0*",
    
    "/sys/bus/mmc",
    "/sys/bus/mmc/drivers/mmcblk",
    "/sys/module/mmc_core",
    "/sys/module/mmcblk",

    // for keys and touchscreen
    "/sys/devices/soc.0/gpio_keys.81/input*",
    "/sys/devices/virtual/input*",
    "/sys/devices/virtual/misc/uinput",
    "/sys/devices/soc.0/f9924000.i2c/i2c-2/2-0020/input*",

    // for adb
    "/sys/devices/virtual/tty/ptmx",
    "/sys/bus/usb",

    // USB drive is in here
    //"/sys/devices/platform/xhci-hcd*",

    // qcom overlay
    "/sys/devices/virtual/misc/ion",
    
    // Encryption
    // "/sys/devices/virtual/misc/device-mapper",
    // "/sys/devices/virtual/qseecom/qseecom",

    NULL
}; 
