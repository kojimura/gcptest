# workflow execution list

```
gcloud workflows executions list workflow-1 \
 --location=us-central1 \
 --format="json" |
 jq -r '.[] | select(type == "object" and .createTime and .duration and .name) | "\(.createTime | split("T")[0]),\(.name | split("/")[-1]),\(.duration | sub("s$"; "") | tonumber)"' \
 > wfex.csv
```

# graph

```
pip install pandas matplotlib
python plot_wf.py

```
