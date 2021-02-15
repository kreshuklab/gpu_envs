#! /bin/bash
module purge
module load $1
path=$(python -c "import $2; print($2.__file__)")
echo $path 
