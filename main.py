def define_env(env):
    @env.macro
    def param(name, p_type, description):
        return f"""<span class="p_name">{name}</span> <span class="p_type">`{p_type}`</span>

{description}

"""

    @env.macro
    def param_bullet(name, p_type, description):
        return f"""
- <span class="p_name">{name}</span> <span class="p_type">`{p_type}`</span>
    {description}
"""