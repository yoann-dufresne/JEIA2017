for filename in `ls ../16s-18s/*.fasta`
do
   file=${filename%.*}
   file=`basename $file` 
   echo $file 
   wgsim -e 0 -d 10 -s 1 -N 100 -1 20 -2 20 -r 0 -R 0 -X 0 -h $filename $file.reads.fq /dev/null
   seqtk seq -A $file.reads.fq > $file.reads.fa
   rm $file.reads.fq
done

cat *.reads.fa | perl seq-shuf > soupe_sequencage.fasta
