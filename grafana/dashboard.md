# [Grouping](https://grafana.com/docs/grafana-cloud/visualizations/dashboards/build-dashboards/create-dashboard/dashboard-groupings/)

You can nest up to three levels deep, which means a dashboard can have a maximum of five configuration levels:
1. Dashboard
2. Grouping 1 - Row or tab
3. Grouping 2 - Row or tab
4. Grouping 3 - Row or tab
5. Panels

## Limit
- Group (Row or Tab) cannot be reused like Library Panel
- watermark **Powered by Grafana** will appear if the dashboard was shared by `Share externally` on Grafana Cloud


## grafana-kiosk
一个独立的浏览器控制器
- [open source](https://github.com/grafana/grafana-kiosk)
- [download: binary only](https://github.com/grafana/grafana-kiosk/releases)
## kiosk mode
在 dashboard URL 后面加：`?kiosk=<value>`
- value `true` in Grafana Cloud: 可以隐藏Grafana logo

