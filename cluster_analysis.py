import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

#load in dataset
df = pd.read_csv('traffic_crash_data.csv')

#drop columns not used for clustering 
df_clustering = df.drop(columns=["Vehicle_Vehicle_Collision", "Vehicle_Pedestrian_Collision"])

#standardize data
X_std = StandardScaler().fit_transform(df_clustering)

#use silhouette analysis to find ideal number of clusters
silhouette_scores = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters = k, random_state = 42, n_init = 10)
    cluster_labels = kmeans.fit_predict(X_std)  
    silhouette_avg = silhouette_score(X_std, cluster_labels)  
    silhouette_scores.append(silhouette_avg) 

#plot silhouette scores
plt.figure(figsize=(8, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.show()

#apply kmeans clustering
kmeans = KMeans(n_clusters = 2, random_state = 42)
df["Cluster"] = kmeans.fit_predict(X_std)

#compare cluster values
cluster_summary = df.groupby("Cluster").mean()
print(cluster_summary)

#calculate average number of each type of collision for each cluster
collision_types = df.groupby("Cluster")[["Vehicle_Pedestrian_Collision", "Vehicle_Vehicle_Collision"]].mean()
print(collision_types)

#perform PCA - reduces dimensions
pca = PCA(n_components = 2)
data = pca.fit_transform(X_std)

#plot clusters
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=df["Cluster"], cmap="viridis", alpha=0.7)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("K-Means Clustering of Traffic Crashes")
plt.colorbar(label="Cluster")
plt.show()