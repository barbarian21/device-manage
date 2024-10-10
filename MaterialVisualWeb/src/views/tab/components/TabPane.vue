<template>
  <el-table :data="list" border fit highlight-current-row style="width: 100%">
    <el-table-column
      v-loading="loading"
      align="center"
      label="ID"
      width="180"
      element-loading-text="请给我点时间！"
    >
      <template slot-scope="scope">
        <span>{{ scope.row.sn }}</span>
      </template>
    </el-table-column>

    <el-table-column width="300px" align="center" label="Date">
      <template slot-scope="scope">
        <!-- <span>{{ scope.row.date_created | parseTime('{y}-{m}-{d} {h}:{i}') }}</span> -->
        <span>{{ scope.row.date_created  }}</span>
      </template>
    </el-table-column>

    <el-table-column min-width="120px" label="Title">
      <template slot-scope="{row}">
        <span>{{ row.card_project }}</span>
        <!-- <el-tag>{{ row.type }}</el-tag> -->
      </template>
    </el-table-column>

    <el-table-column width="110px" align="center" label="Author">
      <template slot-scope="scope">
        <span>{{ scope.row.owner }}</span>
      </template>
    </el-table-column>

    <el-table-column width="120px" label="Importance">
      <template slot-scope="scope">
        <!-- <svg-icon v-for="n in +scope.row.importance" :key="n" icon-class="star" /> -->
         <span>{{ scope.row.name }}</span>
      </template>
    </el-table-column>

    <el-table-column align="center" label="Readings" width="95">
      <template slot-scope="scope">
        <span>{{ scope.row.card_type }}</span>
      </template>
    </el-table-column>

    <el-table-column class-name="status-col" label="Status" width="400">
      <template slot-scope="{row}">
        <el-tag :type="row.device | statusFilter">
          {{ row.remark }}
        </el-tag>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { fetchList } from '@/api/device'
import { parseTime } from '@/utils'

export default {
  filters: {
    statusFilter(status) {
      // if (status === null) {
      //   return 'free'
      // }
      
      return 'buzzy'
    }
  },
  props: {
    type: {
      type: String,
      default: 'Pavo'
    }
  },
  data() {
    return {
      list: null,
      listQuery: {
        // page: 1,
        // limit: 5,
        card_project: this.type,
        // sort: '+id'
      },
      loading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.loading = true
      // this.$emit('create') // for test
      fetchList(this.listQuery).then(response => {
        this.list = response.data.results
        this.loading = false
      })
    }
  }
}
</script>

