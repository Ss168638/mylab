# === codegen/generator.py ===
def generate_c_code(components):
    code = "#include <stdio.h>\n#include <math.h>\n\nfloat bp_signal[1000];\nvoid simulate() {\n"
    for c in components:
        if c.name == "Gain":
            code += f"    for(int i=0;i<1000;i++) bp_signal[i] *= {c.params['gain']};\n"
        elif c.name == "LowPassFilter":
            code += "    // Low pass filter logic here (to be implemented manually in C)\n"
        elif c.name == "ADC":
            code += f"    for(int i=0;i<1000;i++) bp_signal[i] = round(bp_signal[i] * {c.params['levels']}) / {c.params['levels']};\n"
    code += "}\n\nint main() { simulate(); return 0; }"
    return code