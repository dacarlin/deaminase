from autoprotocol import Protocol 
import json 

p = Protocol()

# refs 
wash = p.ref( 'wash', cont_type='96-deep', discard=True )
elute = p.ref( 'elute', cont_type='96-deep', discard=True ) 
adenosine = p.ref( 'adenosine', cont_type='96-deep', discard=True )
mutants = [ p.ref( 'm{}'.format( m ), cont_type='micro-2.0', discard=True ) for m in '0123' ] 

# manually set volumes for testing 
wash.wells( 0, 95 ).set_volume( '200:microliter' ) 
elute.wells( 0, 95 ).set_volume( '200:microliter' )

# make substrate plate 
p.distribute



if __name__ == '__main__':
  print json.dumps( p.as_dict(), indent=2 ) 
