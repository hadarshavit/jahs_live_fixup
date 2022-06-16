from jahs_bench_201 import api


def run():
    b = api.Benchmark(task="cifar10", kind="surrogate", download=True)
    config, results = b.random_sample()
    print(f"Sampled random configuration: {config}\nResults of query on the surrogate "
          f"model: {results}")

if __name__ == "__main__":
    run()