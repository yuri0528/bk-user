<!--
  - TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-用户管理(Bk-User) available.
  - Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
  - Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
  - You may obtain a copy of the License at http://opensource.org/licenses/MIT
  - Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
  - an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
  - specific language governing permissions and limitations under the License.
  -->
<template>
  <div :class="['input-text', { 'mark-red': item.isError }]">
    <bk-date-picker
      font-size="14"
      class="king-date-picker"
      :placeholder="$t('请选择日期')"
      :value="item.value"
      :disabled="editStatus && !item.editable"
      :options="starttimePickerOptions"
      @change="changeDate">
    </bk-date-picker>
    <p class="hint" v-show="item.isError">
      <i class="arrow"></i>
      <i class="icon-user-exclamation-circle-shape"></i>
      <span class="text">{{$t('请填写正确')}}{{item.name}}</span>
    </p>
  </div>
</template>

<script>
import moment from 'moment';
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
    editStatus: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      starttimePickerOptions: {},
    };
  },
  mounted() {
    // 初始化高级配置启动时间
    this.starttimePickerOptions = {
      disabledDate(time) {
        return (
          time.getTime() < moment(new Date())
            .subtract(1, 'days')
            .valueOf()
        );
      },
    };
  },
  methods: {
    changeDate(date) {
      // eslint-disable-next-line vue/no-mutating-props
      this.item.value = date;
      // eslint-disable-next-line vue/no-mutating-props
      this.item.isError = false;
    },
  },
};
</script>

<style lang="scss">
.input-text .king-date-picker {
  width: 100%;
}

.mark-red .king-date-picker input {
  border: 1px solid #ea3636;
}
</style>

<style lang="scss" scoped>
.hint {
  padding: 10px;
  position: absolute;
  top: -42px;
  right: 0;
  color: #fff;
  font-size: 0;
  border-radius: 4px;
  background: rgba(0, 0, 0, .8);;

  .arrow {
    position: absolute;
    bottom: -2px;
    right: 14px;
    width: 6px;
    height: 6px;
    border-top: 1px solid #000;
    border-left: 1px solid #000;
    transform: rotate(45deg);
    z-index: 10;
    background: #000;
  }

  .text,
  .icon-user-exclamation-circle-shape {
    display: inline-block;
    vertical-align: middle;
    font-size: 12px;
  }

  .icon-user-exclamation-circle-shape {
    font-size: 16px;
    margin-right: 10px;
    position: relative;
    right: 0;
    top: 0;
    color: #fff;
  }
}
</style>
