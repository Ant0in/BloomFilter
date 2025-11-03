
import math
import numpy as np
import matplotlib.pyplot as plt
from src import BloomFilter


def theoretical_fp(m: int, n: int, k: int) -> float:
    """Theoretical false positive rate of a Bloom filter."""
    return (1 - math.exp(-k * n / m)) ** k

def measure_fp(m: int, n: int, k: int, tests: int = 10000, seeds: list[int] = [42]) -> float:
    """Run Bloom filter and return average measured false positive rate."""
    fps = []
    for seed in seeds:
        bf = BloomFilter.New(m=m, k=k, seed=seed)
        for i in range(n):
            bf.add(i)
        false_positives = sum(bf.check(i) for i in range(n, n + tests))
        fps.append(false_positives / tests)
    return np.mean(fps), np.std(fps)

# ------------------------------
# 1) FP vs k (exhaustive sweep)
m = 10000
n = 500
tests = 20000
k_opt = round((m / n) * math.log(2))
k_values = list(range(1, k_opt*3 + 1))
measured = []
measured_std = []
theoretical = []

for k in k_values:
    fp_mean, fp_std = measure_fp(m, n, k, tests, seeds=[42, 43, 44])
    measured.append(fp_mean)
    measured_std.append(fp_std)
    theoretical.append(theoretical_fp(m, n, k))

plt.figure(figsize=(8,5))
plt.plot(k_values, theoretical, label="Theoretical FP", marker='o')
plt.errorbar(k_values, measured, yerr=measured_std, fmt='x', label="Measured FP ± std")
plt.axvline(k_opt, color='gray', linestyle='--', label=f"Optimal k ≈ {k_opt}")
plt.xlabel("Number of hash functions k")
plt.ylabel("False positive rate")
plt.title(f"Bloom Filter FP vs k (n={n}, m={m})")
plt.legend()
plt.grid(True)
plt.savefig("FP_vs_k.png", dpi=300)

# ------------------------------
# 2) FP vs m/n ratio
m_values = [5000, 10000, 20000, 40000]
k_values_mn = [round((m_val / n) * math.log(2)) for m_val in m_values]
measured_fp = []
theoretical_fp_values = []

for m_val, k_val in zip(m_values, k_values_mn):
    fp_mean, _ = measure_fp(m_val, n, k_val, tests, seeds=[42,43,44])
    measured_fp.append(fp_mean)
    theoretical_fp_values.append(theoretical_fp(m_val, n, k_val))

plt.figure(figsize=(8,5))
plt.plot([m_val/n for m_val in m_values], theoretical_fp_values, 'o-', label="Theoretical FP")
plt.plot([m_val/n for m_val in m_values], measured_fp, 'x-', label="Measured FP")
plt.xlabel("Bits per element (m/n)")
plt.ylabel("False positive rate")
plt.title(f"Bloom Filter FP vs m/n ratio (n={n})")
plt.legend()
plt.grid(True)
plt.savefig("FP_vs_mn.png", dpi=300)

# ------------------------------
# 3) FP vs n (load factor)
m_fixed = 10000
n_values = list(range(100, 1001, 100))
measured_fp_n = []
theoretical_fp_n = []

for n_val in n_values:
    k_val = round((m_fixed / n_val) * math.log(2))
    fp_mean, _ = measure_fp(m_fixed, n_val, k_val, tests, seeds=[42,43,44])
    measured_fp_n.append(fp_mean)
    theoretical_fp_n.append(theoretical_fp(m_fixed, n_val, k_val))

plt.figure(figsize=(8,5))
plt.plot(n_values, theoretical_fp_n, 'o-', label="Theoretical FP")
plt.plot(n_values, measured_fp_n, 'x-', label="Measured FP")
plt.xlabel("Number of inserted elements n")
plt.ylabel("False positive rate")
plt.title(f"Bloom Filter FP vs n (m={m_fixed})")
plt.legend()
plt.grid(True)
plt.savefig("FP_vs_n.png", dpi=300)

# ------------------------------
# 4) Heatmap: FP over k and n/m ratio
k_range = list(range(1, 30))
nm_ratios = np.linspace(0.05, 0.5, 10)  # n/m from small to moderate
fp_matrix = np.zeros((len(k_range), len(nm_ratios)))

for i, k_val in enumerate(k_range):
    for j, nm in enumerate(nm_ratios):
        n_val = int(m_fixed * nm)
        fp_matrix[i,j], _ = measure_fp(m_fixed, n_val, k_val, tests=5000, seeds=[42])

plt.figure(figsize=(8,5))
plt.imshow(fp_matrix, origin='lower', aspect='auto',
           extent=[nm_ratios[0], nm_ratios[-1], k_range[0], k_range[-1]],
           cmap='viridis')
plt.colorbar(label='Measured FP rate')
plt.xlabel("Load factor n/m")
plt.ylabel("Number of hash functions k")
plt.title("Bloom Filter FP rate heatmap")
plt.savefig("FP_heatmap.png", dpi=300)
