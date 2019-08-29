# graphene-cerberus
A (work-in-progress) package for more convenient interfacing between the Graphene/graphql-core system and the Cerberus validation package. Tested with Graphene 2.1.5 and Cerberus 1.3.1 

### What it does:

Currently, gives you a meta decorator titled
`validate_input()` for the mutate and resolve class methods that optionally takes in:
```
validator: Validator (required) -- A cerberus validator instance
enforce_allow_unknown: bool (default True) -- Setting this to False requires that your validation schema contain every possible argument for your mutate call.
auto_camelcase: bool (default True) -- Whether the validation error returned to clients should be camel cased or not (this is a good idea if you keep the default option for camel casing fields in your GQL schema)
extensions_param_name: str (default 'invalidArgs') -- what to name the field inside of extensions containing the errors. To be used for later functionality.
error_message : str (default 'Invalid Arguments Provided by Client!') -- what the actual error message returned to the client should be.
```

The implementation is framework-agnostic, meaning it works perfectly for whatever graphene-based stack you are using. In its current iteration, development will be based around requirements of my Flask/SQLAlchemy/GraphQL stack, but those packages will never be required or encouraged.

## Todo:

The long-term goal for this project is to wrap graphene Fields in a way that is compatible with current Mutation/Query objects, and manipulate or either provide a decorator for resolve/mutate. For now, it's a tool of convenience for people not looking to waste time writing their own custom decorator.
