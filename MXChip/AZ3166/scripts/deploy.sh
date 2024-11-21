#  Copyright (c) Microsoft
#  Copyright (c) 2024 Eclipse Foundation
#
#  This program and the accompanying materials are made available
#  under the terms of the MIT license which is available at
#  https://opensource.org/license/mit.
#
#  SPDX-License-Identifier: MIT
#
#  Contributors:
#     Microsoft         - Initial version
#     Frédéric Desbiens - 2024 version.

#!/bin/bash

# Use paths relative to this script's location
SCRIPT=$(readlink -f "$0")
SCRIPTDIR=$(dirname "$SCRIPT")
BASEDIR=$(dirname "$SCRIPTDIR")

# echo $BASEDIR

# If you want to build into a different directory, change this variable
BUILDDIR="$BASEDIR/build"

# And then do the build
cmake --build $BUILDDIR

cp $BUILDDIR/app/mxchip_threadx.bin /Volumes/AZ3166
