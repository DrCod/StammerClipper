#!/bin/bash

# Usage : scp_ext_dsf_feat.sh dsf_img_directory output_file

dsf_img_dir=$1
out_file=$2

[ -z "$dsf_img_dir" ] && echo "error!! need to dsf_img_directory" && exit 1;
[ -z "$out_file" ] && echo "error!! need to output_file" && exit 1;

cd df_detector
find $dsf_img_dir -iname "*.dsf_img" > $dsf_img_dir/dsfimglist.log

rm -f $out_file
touch $out_file

# output for EST 
# speaker set task feat1 feat2 feat3 ...
while read line
do
  dsf_img_file=$line
  speaker=$(echo $line | sed 's#.*/[FM]*_[0-9]*_\([A-Z]*\)_[0-9]*\.dsf_img#\1#g')
  setnum=$(echo $line | sed 's#.*/[FM]*_\([0-9]*\)_[A-Z]*_[0-9]*\.dsf_img#\1#g')
  tasknum=$(echo $line | sed 's#.*/[FM]*_[0-9]*_[A-Z]*_\([0-9]*\)\.dsf_img#\1#g')
  echo -n "$speaker $setnum $tasknum " >> $out_file
  ext_dsffeat_dsfimg.py $dsf_img_file >> $out_file

done < $dsf_img_dir/dsfimglist.log

# general output
# filename feat1 feat2 feat3 ...
: << 'General'
while read line
do
  dsf_img_file=$line
  target_file=$(echo $line | sed 's#.*/\([A-Za-z_0-9]*\)\.dsf#\1#g')
  
  echo -n "$target_file " >> $out_file
  ext_dsffeat_dsfimg.py $dsf_img_file >> $out_file

done < $dsf_img_dir/dsfimglist.log
General

: << 'END'
usage: ext_dsffeat_dsfimg.py [-h] [-m OUTMODE] [-o OUTFILE] dsf_img_file

positional arguments:
  dsf_img_file  input dsfimg file name

optional arguments:
  -h, --help    show this help message and exit
  -m OUTMODE    the mode of output : outscreen (default), pckout, txtappend
  -o OUTFILE    the output file name for pckout or txtappend of outmode
END
