def grow( protocol, params ):
  protocol.dispense_full_plate( params['plate'], 'tb-broth-50ug-ml-kan', '1:milliliter' )

from autoprotocol.harness import run
if __name__ == '__main__':
  run( grow, "grow" ) 
