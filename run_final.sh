if [ $# -ne 1 ]; then
   echo "Usage: $0 <input_file>"
   exit 1
fi

if [ $1 -eq 1 ]; then
   ./run_mod.sh
fi

if [ $1 -eq 0 ]; then
   ./run_unmod.sh
fi