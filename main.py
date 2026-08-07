def define_env(env):
    @env.macro
    def param(name, p_type, p_description):
        return f"""<span class="p_name">{name}</span> <span class="p_type">`{p_type}`</span>

<span class="p_description">{p_description}</span>

"""

    @env.macro
    def param_bullet(name, p_type, p_description, p_extra=None):
        if p_extra:
            return f"""
- <span class="p_name">{name}</span> <span class="p_type">`{p_type}`</span>

    <span class="p_description">{p_description}</span>
    
    <span class="p_extra">{p_extra}</span>
"""
        return f"""
- <span class="p_name">{name}</span> <span class="p_type">`{p_type}`</span>

    <span class="p_description">{p_description}</span>
"""