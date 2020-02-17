
import particles
import couplings
import lorentz
import parameters
import vertices
import coupling_orders
import write_param_card
import propagators


all_particles = particles.all_particles
all_vertices = vertices.all_vertices
all_couplings = couplings.all_couplings
all_lorentz = lorentz.all_lorentz
all_parameters = parameters.all_parameters
all_orders = coupling_orders.all_orders
all_functions = function_library.all_functions
all_propagators = propagators.all_propagators

try:
   import form_factors
except ImportError:
   pass
else:
   all_form_factors = form_factors.all_form_factors

try:
   import assumptions
except ImportError:
   all_assumptions = []
else:
   all_assumptions = assumptions.all_assumptions

def add_decays(error=True):
   global all_decays
   try:
      import decays
   except ImportError:
      if error:
         raise
      else:
         return False
   else:
      all_decays = decays.all_decays
      return all_decays

def add_NLO(error=True):
   global CT_vertices, CT_couplings
   try:
      import CT_vertices
      import CT_couplings
   except ImportError:
      if error:
         raise
      else:
         return False
   else:      
      all_CTvertices = CT_vertices.all_CTvertices
      all_CTcouplings = CT_couplings.all_CTcouplings
      return all_CTvertices, all_CTcouplings

def add_restriction(error=True):
   global all_restrictions
   try:
      import restrictions
   except ImportError:
      if error:
         raise
      else:
         return False
   else:      
      all_restrictions = restrictions.all_restrictions
      return all_restrictions


gauge = [0]


__author__ = "Benjamin Fuks"
__date__ = "20.03.12"
__version__= "1.0.3"
