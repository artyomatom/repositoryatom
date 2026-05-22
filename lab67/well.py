def register_methods(cls):
   
    cls.methods = [attr for attr in dir(cls) if not attr.startswith('_') and callable(getattr(cls, attr))]
    return cls

@register_methods
class MathOps:
    def add(self, a, b):
        return a + b
    
    def mul(self, a, b):
        return a * b

print(MathOps.methods)  # ['add', 'mul']
