# Hexagonal-Architecture-Project-Template-Python
Template to be used for Hexagonal Architecture projects in python

## Why use this architecture
- Implements a expressive architecture that helps make the code extensible
- Makes it easy to communicate between devs and add new features. The architecture moves from an abstract concept to one that is implemented in code and can be taught to new people joining the team.

## Architecture details
- The top level "model" folder indicates the module will be implementing use cases around "model"
- The "domain" package contains the class definintnion of the modl
- The "application" folder contains a service layer around the domain
    - The "ModelService" implements the incoming port interface and uses the outgoing port interfaces
- The adapter packages contains incoming and outgoing adapters that call the application layers's incoming and outpoing ports.

## Explanation of Various Componenets
### Port
- An interface that will be implemented by the adapter. The application layer calls the port interface to call the functionality of the adapter
    - ### Use Case
    - The perform the following
        1. Take input
        2. Validate business rules
        3. Manipulate model state: e.g change state and pass it to a port implemented by an adapter
        4. Return output: Translate return value from the outpgoing adapter into an output object that will be returned to the callign adapter

    - 

### Adapter

### Service