#
# Copyright (C) 2016 Exodus Android
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""Emit commands needed for OnePlus2 during OTA installation
(installing the firmware images)."""

import common
import re
import sha

def FullOTA_Assertions(info):
  print "FullOTA_Assertions not implemented"

def IncrementalOTA_Assertions(info):
  print "IncrementalOTA_Assertions not implemented"

def InstallImage(img_name, img_file, partition, info):
  common.ZipWriteStr(info.output_zip, img_name, img_file)
  info.script.AppendExtra(('package_extract_file("' + img_name + '", "/dev/block/bootdevice/by-name/' + partition + '");'))

image_partitions = {
   'NON-HLOS.bin'      : 'modem',
   'static_nvbk.bin'   : 'oem_stanvbk',
   'emmc_appsboot.mbn' : 'aboot',
   'rpm.mbn'           : 'rpm',
   'sdi.mbn'           : 'sdi',
   'sbl1.mbn'          : 'sbl1',
   'pmic.mbn'          : 'pmic',
   'tz.mbn'            : 'tz',
   'hyp.mbn'           : 'hyp',
   'BTFM.bin'          : 'bluetooth',
}

def FullOTA_InstallEnd(info):
  info.script.Print("Writing recommended Exodus Firmware...")
  for k, v in image_partitions.iteritems():
    try:
      img_file = info.input_zip.read("RADIO/" + k)
      InstallImage(k, img_file, v, info)
    except KeyError:
      print "warning: no " + k + " image in input target_files; not flashing " + k


def IncrementalOTA_InstallEnd(info):
  for k, v in image_partitions.iteritems():
    try:
      source_file = info.source_zip.read("RADIO/" + k)
      target_file = info.target_zip.read("RADIO/" + k)
      if source_file != target_file:
        InstallImage(k, target_file, v, info)
      else:
        print k + " image unchanged; skipping"
    except KeyError:
      print "warning: " + k + " image missing from target; aborting: " + k
