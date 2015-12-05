import screed 
for record in screed.open( 'manual_trim.fasta' ):
  codons = [ record.sequence[i:i+3] for i in range( 0, len( record.sequence ), 3 ) ] 
  amino_acids = [ '666' ] 

  for i, codon in enumerate( codons ):
    if 5 < i < len( codons ) - 5:

      print '---'
      print 'original codon:', codon 
      print 'original region:', codons[i-4:i+5] #gives 3 * 4 = 12 bp on each side, 12 + 12 + 3 = 27 bp oligo  
      print 'left flank:', codons[i-4:i]
      print 'right flank:', codons[i+1:i+5] 

      for j, aa in enumerate( amino_acids ):
        print 'new codon:', aa
        print 'new region:', codons[i-4:i] + [ aa ] + codons[i+1:i+5] 
