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