#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
HUB_DIR=$( dirname "$SCRIPT_DIR")
FOLDERS=("ia-datafortelling" "fia-datafortelling")

for folder in ${FOLDERS[@]}; do
  REQUIREMENTS_FILE="$HUB_DIR/$folder/requirements.txt"
  if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "$folder:"
    python3 -m venv "$HUB_DIR/$folder/venv"
    source "$HUB_DIR/$folder/venv/bin/activate"
    echo " virtuelt miljø lagd.."
    echo " installerer requirements.txt i virtuelt miljø.. (dette kan ta litt tid)"
    pip install -r "$REQUIREMENTS_FILE" > /dev/null 2>&1
    echo " requirements.txt installert.."
    echo ""
    echo "Utdaterte pakker:"
    echo ""

    new_requirements=""

    while read -r line; do
      package=$(echo $line | awk '{print $1}')
      current_version=$(echo $line | awk '{print $2}')
      latest_version=$(echo $line | awk '{print $3}')
      echo "Pakke: $package"
      echo "Gjeldende version: $current_version"
      echo "Siste version: $latest_version"
      echo "Versjonshistorikk: https://pypi.org/project/$package/$latest_version/#history"
      echo ""
      new_requirements+="$package==$latest_version"$'\n'
    done <<< "$(pip list --outdated | tail -n +3)"

    echo "Pakker som kanskje bør oppdateres:"
    echo "$new_requirements"

    deactivate
    rm -rf "$HUB_DIR/$folder/venv"
    echo "Cleanup - virtuelt miljø slettet"
    echo ""
  else
    echo "$folder: requirements.txt ikke funnet"
  fi
done