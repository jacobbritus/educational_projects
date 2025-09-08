# CLI to-do list

The second project for this repository.

I initially made it 3 months ago, but now I'll finish, improve and represent it here.

It differentiates from basic to-do lists by being customizable and the readchar module which reads keyboard input which allows for quick and flexible executions.

**Features**
- Listing tasks
- Changing keybinds
- Changing colors (to be done)

**Improvements**
- Mapping page variants in a dict rather than conditionals.
- Using a create box function which got rid of a lot of DRY.
  - I got to use my fresh learnt knowledge on **kwargs.
- Using ```key = list(dict.keys()) → dict[key]``` to index dict keys


