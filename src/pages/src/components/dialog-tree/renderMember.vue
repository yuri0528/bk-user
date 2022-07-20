<template>
  <render-horizontal-block
    :label="$t('启用范围')">
    <section class="action-wrapper" @click.stop="handleAddMember" data-test-id="grading_btn_showAddMember">
      <i class="bk-icon icon-plus-circle-shape plus-circle-shape" />
      <span>{{ $t('添加范围') }}</span>
    </section>
    <div :class="['action-content', { 'is-active': isActive }]">
      <div style="margin-top: 9px;" v-if="isAll">
        <div class="all-item">
          <span class="member-name">{{ $t('全员') }}</span>
          <span class="display-name">(All)</span>
          <i class="user-icon icon-close-fill remove-icon" @click="handleDelete" />
        </div>
      </div>
      <template v-else>
        <render-member-item :data="users" @on-delete="handleDeleteUser" v-if="isHasUser" />
        <render-member-item
          :data="departments" type="department" v-if="isHasDepartment"
          @on-delete="handleDeleteDepartment" />
      </template>
      <bk-button
        class="submit-button"
        theme="primary" type="button" @click="handleSubmit"
        data-test-id="grading_btn_createSubmit"
        :disabled="isDisabled"
        :loading="submitLoading">
        {{ $t('提交') }}
      </bk-button>
    </div>
  </render-horizontal-block>
</template>
<script>
import RenderHorizontalBlock from './renderHorizontalBlock.vue';
import RenderMemberItem from './RenderMemberDisplay.vue';
export default {
  components: {
    RenderHorizontalBlock,
    RenderMemberItem,
  },
  props: {
    users: {
      type: Array,
      default: () => [],
    },
    departments: {
      type: Array,
      default: () => [],
    },
    isAll: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isDisabled: true,
    };
  },
  computed: {
    isHasUser() {
      return this.users.length > 0;
    },
    isHasDepartment() {
      return this.departments.length > 0;
    },
    changeDate() {
      const { isAll, departments, users } = this;
      return {
        isAll,
        departments,
        users,
      };
    },
    isActive() {
      return this.isHasUser || this.isHasDepartment || this.isAll;
    },
  },
  watch: {
    changeDate(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.isDisabled = false;
      }
    },
  },
  methods: {
    handleAddMember() {
      this.$emit('on-add');
    },
    handleDeleteUser(payload) {
      this.$emit('on-delete', 'user', payload);
    },
    handleDeleteDepartment(payload) {
      this.$emit('on-delete', 'department', payload);
    },
    handleDelete() {
      this.$emit('on-delete-all');
    },
    handleSubmit() {
      this.isDisabled = true;
    },
  },
};
</script>
<style lang="postcss" scoped>
.action-wrapper {
  margin-left: 8px;
  display: inline-block;
  font-size: 14px;
  color: #3a84ff;
  cursor: pointer;
  &:hover {
    color: #699df4;
  }
  i {
    position: relative;
    top: -1px;
    left: 2px;
  }
}
.action-content {
  max-width: 800px;
  margin: 10px;
  position: relative;
  padding: 10px;
  .submit-button {
    position: absolute;
    bottom: -43px;
    right: 0;
  }
}
.is-active {
  border: 1px solid #dcdee5;
}
.all-item {
  position: relative;
  display: inline-block;
  margin: 0 6px 6px 10px;
  padding: 0 10px;
  line-height: 22px;
  background: #f5f6fa;
  border: 1px solid #dcdee5;
  border-radius: 2px;
  font-size: 14px;
  &:hover {
    .remove-icon {
      display: block;
    }
  }
  .member-name {
    display: inline-block;
    max-width: 200px;
    line-height: 17px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    vertical-align: text-top;
    .count {
      color: #c4c6cc;
    }
  }
  .display_name {
    display: inline-block;
    vertical-align: top;
  }
  .remove-icon {
    display: none;
    position: absolute;
    top: -6px;
    right: -6px;
    cursor: pointer;
  }
}
</style>
