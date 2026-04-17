<%*
let d = moment(tp.file.title, "YYYY-MM-DD");
let q = "Q" + (Math.floor(d.month() / 3) + 1);
let w = d.isoWeek().toString().padStart(2, '0');
-%>
---
week: '[[<% d.format("YYYY") %>-W<% w %>]]'
date: '<% tp.file.title %>'
cssclasses:
  - hide-properties
  - daily
  <% "- " + tp.date.now("dddd", 0, tp.file.title, "YYYYMMDD").toLowerCase() %>
---

## [[<% d.format("YYYY")%>]] / [[<%d.format("YYYY")%>-<% q %>|<% q %>]] / [[<% d.format("YYYY-MM") %>|<% d.format("MMMM") %>]] / [[<% d.format("YYYY") %>-W<% w %>|Week <% d.isoWeek() %>]]
# DAILY NOTE
##### ❮ [[<% d.clone().subtract(1, 'days').format("YYYY-MM-DD") %>]] | <% tp.file.title %> | [[<% d.clone().add(1, 'days').format("YYYY-MM-DD") %>]] ❯
---
### 📕Freewrite




---
### 📜Tasks

#### 🏗️Work
- [ ] 盛天学院每日签到
- [ ] 

#### 📝Study
- [ ] 

---
### ⚛️Habits

- 🧘🏻[meditation::]
- 📖[reading::]
- 🏋🏻‍♂️[workout::]

#### End-of-Day Checklist
- [ ] Backup Vault
---

<%*
let birth = "1998-11-23";
let death = moment(birth).add(80, 'years');
let daysLeft = death.diff(moment(tp.file.title, "YYYY-MM-DD"), 'days');
%>
> [!error] 死亡倒计时：**<% daysLeft %> 天**

![[On This Day.base]] 

