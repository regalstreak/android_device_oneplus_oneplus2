LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

ifeq ($(ADD_RADIO_FILES), true)
radio_dir := $(LOCAL_PATH)/radio
RADIO_FILES := $(shell cd $(radio_dir) ; ls)
$(foreach f, $(RADIO_FILES), \
    $(call add-radio-file,radio/$(f)))
endif

#radio file
$(call add-radio-file,firmware/NON-HLOS.bin)
#static_nvbk image
$(call add-radio-file,firmware/static_nvbk.bin)
#emmc_appsboot image
$(call add-radio-file,firmware/emmc_appsboot.mbn)
#rpm image
$(call add-radio-file,firmware/rpm.mbn)
#sbl1 image
$(call add-radio-file,firmware/sbl1.mbn)
#sdi image
$(call add-radio-file,firmware/sdi.mbn)
#pmic image
$(call add-radio-file,firmware/pmic.mbn)
#tz version image
$(call add-radio-file,firmware/tz.mbn)
#hyp.mbn image
$(call add-radio-file,firmware/hyp.mbn)
#Bluetooth image
$(call add-radio-file,firmware/BTFM.bin)
