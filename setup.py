from distutils.core import setup, Extension
import sysconfig

def main():
    CFLAGS = ['-g', '-Wall', '-std=c99', '-fopenmp', '-mavx', '-mfma', '-pthread', '-O3']
    LDFLAGS = ['-fopenmp']
    # Use the setup function we imported and set up the modules.
    # You may find this reference helpful: https://docs.python.org/3.6/extending/building.html
    # TODO: YOUR CODE HERE
    setup(name="numc",
        version="0.0.1",
        description="numc matrix operations",
        ext_modules=[
        Extension("numc",
                    sources=["numc.c", "matrix.c"],
                    extra_compile_args=CFLAGS,
                    extra_link_args=LDFLAGS,
                    language='c')
        ])
    setup(name="dumbc",
            version="0.0.1",
            description="numc_naive matrix operations",
            ext_modules=[
            Extension("dumbc",
                        sources=["numc.c", "matrix_naive.c"],
                        extra_compile_args=CFLAGS,
                        extra_link_args=LDFLAGS,
                        language='c')
            ])
if __name__ == "__main__":
    main()
