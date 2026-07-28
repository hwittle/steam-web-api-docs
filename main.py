def define_env(env):
    @env.macro
    def param(name, type, description):
        return f"""
#### {name} <span class="param-type">{type}</span>
{description}
"""