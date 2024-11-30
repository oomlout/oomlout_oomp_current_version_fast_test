import action_build_oomp



import cProfile
import pstats
import action_build_oomp
import os

def main(**kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Your main function code here
    action_build_oomp.main(**kwargs)  # Replace with the actual function call
    
    profiler.disable()
    profiler.dump_stats('profile_output.prof')
    print("Profile data saved to profile_output.prof. Use 'snakeviz profile_output.prof' to visualize.")

    #launch visualizer
    os.system("snakeviz profile_output.prof")
 


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)