from scipy import stats

def ttest_two_samples(sample1, sample2):
    """Perform t-test between two samples."""
    return stats.ttest_ind(sample1, sample2)
