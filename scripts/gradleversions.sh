SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
HUB_DIR=$( dirname "$SCRIPT_DIR")

find $HUB_DIR -type f -name gradlew -exec echo --- {} --- \; -exec {} -v \;
