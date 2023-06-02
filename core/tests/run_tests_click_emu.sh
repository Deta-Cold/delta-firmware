#!/usr/bin/env bash

: "${RUN_TEST_EMU:=1}"

CORE_DIR="$(SHELL_SESSION_FILE='' && cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"
MICROPYTHON="${MICROPYTHON:-$CORE_DIR/build/unix/detahard-emu-core}"
detahard_SRC="${CORE_DIR}/src"

DISABLE_ANIMATION=1
PYOPT="${PYOPT:-0}"
upy_pid=""

# run emulator if RUN_TEST_EMU
if [[ $RUN_TEST_EMU > 0 ]]; then
  source ../detahard_cmd.sh

  # remove flash and sdcard files before run to prevent inconsistent states
  mv "${detahard_PROFILE_DIR}/detahard.flash" "${detahard_PROFILE_DIR}/detahard.flash.bkp" 2>/dev/null
  mv "${detahard_PROFILE_DIR}/detahard.sdcard" "${detahard_PROFILE_DIR}/detahard.sdcard.bkp" 2>/dev/null

  cd "${detahard_SRC}"
  echo "Starting emulator: $MICROPYTHON $ARGS ${MAIN}"

  detahard_TEST=1 \
  detahard_DISABLE_ANIMATION=$DISABLE_ANIMATION \
    $MICROPYTHON $ARGS "${MAIN}" &> "${detahard_LOGFILE}" &
  upy_pid=$!
  cd -
  sleep 30
fi

# run tests
error=0
if ! pytest --junitxml=../../tests/junit.xml ../../tests/click_tests "$@"; then
  error=1
fi
kill $upy_pid
exit $error
