# Gitcoin Beta Round Analysis

This GitHub repo serves as the submission for the during and after round analysis of the Gitcoin Beta round. The analysis took account of the data that was being updated during the round and the final update after the round. The purpose of this analysis was to identify Sybil attacks in the Gitcoin ecosystem and assess the effectiveness of measures taken to prevent such attacks.

## Contents

This repo contains the code and results of the analysis conducted during and after the Gitcoin Beta round. The contents of the repo include:

The repository is structured as follows:

- **identified_sybils folder**: holds the list of identified Sybils for the alpha round that was used for post mortem analysis and also the beta round identified Sybils.
- **queried_data folder**: contains all the wallet information queried for each supporter address.
- **sybil_research_data folder**: contains the data provided by the ODC for the beta and alpha round (which is currently replaced with a link to the dataset on Ocean.)
- **voters folder**: contains the list of voters and their votes to grants alpha and beta round (which is currently replaced with a link to the dataset on Ocean.)
- **report.pdf**: a summary of the analytics process.
- **voters.ipynb**: a Jupyter notebook that houses all the code used.
- **TDD**: a script that calculates the TDD (Transaction Date Mean Difference).

## Usage

To use this repo, you can clone or download the repo to your local machine and run the analysis code to replicate the results. The results can be viewed in the `identified_sybils` folder.

## Conclusion

The analysis presented in this GitHub repo provides insights into the prevalence and patterns of Sybil attacks in the Gitcoin Beta round and highlights the need for better measures to prevent such attacks. By detecting and mitigating Sybil attacks, the Gitcoin platform can ensure the integrity of the ecosystem and continue to serve as a reliable and trustworthy space for funding open-source projects.
