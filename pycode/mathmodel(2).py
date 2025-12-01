import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation
import matplotlib as mpl

# ----------------------
# 设置中文字体，解决中文显示问题
# ----------------------
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# ----------------------
# 1. 定义生态系统模型（七鳃鳗+宿主+捕食者）
# ----------------------
def ecosystem_model(state, t, resource_level):
    # state = [七鳃鳗雄性数量, 七鳃鳗雌性数量, 宿主种群数量, 捕食者种群数量]
    m, f, h, p = state
    
    # 七鳃鳗性别比例由资源决定（背景：资源少→雄性多，资源多→雌性多）
    # 资源水平：0=匮乏, 1=充足；雄性比例：资源少→78%，资源多→56%
    male_ratio = 0.78 if resource_level < 0.5 else 0.56
    female_ratio = 1 - male_ratio
    
    # 七鳃鳗繁殖率（雌性数量决定产卵量）
    eel_birth = 0.8 * f  # 每只雌性的繁殖系数
    # 七鳃鳗死亡率（受捕食者影响）
    eel_death = 0.1 * (m + f) + 0.02 * p * (m + f)
    
    # 宿主种群（被七鳃鳗寄生）
    host_birth = 0.5 * h
    host_death = 0.05 * h + 0.03 * (m + f) * h  # 寄生导致死亡
    
    # 捕食者种群（以七鳃鳗为食）
    predator_birth = 0.04 * p * (m + f)
    predator_death = 0.2 * p
    
    # 性别比例动态调整（幼体按资源比例分化为雌雄）
    d_m = (male_ratio * eel_birth) - eel_death
    d_f = (female_ratio * eel_birth) - eel_death
    d_h = host_birth - host_death
    d_p = predator_birth - predator_death
    
    return [d_m, d_f, d_h, d_p]

# ----------------------
# 2. 模拟不同资源条件下的生态系统变化
# ----------------------
# 初始状态：[雄性, 雌性, 宿主, 捕食者]
initial_state = [78, 22, 1000, 50]  # 资源匮乏时初始性别比78:22
t = np.linspace(0, 50, 200)  # 模拟50个时间单位

# 模拟两种资源场景
# 场景1：资源匮乏（前25个时间单位）→ 场景2：资源充足（后25个时间单位）
resource_levels = np.concatenate([np.zeros(100), np.ones(100)])

# 数值求解微分方程
states = []
current_state = initial_state.copy()
for i in range(len(t)-1):
    # 每个时间步长用当前资源水平求解
    t_step = [t[i], t[i+1]]
    res = odeint(ecosystem_model, current_state, t_step, args=(resource_levels[i],))
    current_state = res[-1]
    states.append(current_state)
states = np.array(states)

# ----------------------
# 3. 可视化结果
# ----------------------
plt.figure(figsize=(14, 10))

# 子图1：七鳃鳗雌雄数量+性别比例
plt.subplot(2,2,1)
plt.plot(t[1:], states[:,0], label='七鳃鳗雄性', color='blue', linewidth=2)
plt.plot(t[1:], states[:,1], label='七鳃鳗雌性', color='pink', linewidth=2)
plt.axvline(x=25, color='gray', linestyle='--', alpha=0.7, label='资源从匮乏→充足')
plt.title('七鳃鳗种群动态', fontsize=14, fontweight='bold')
plt.xlabel('时间')
plt.ylabel('种群数量')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# 子图2：性别比例
plt.subplot(2,2,2)
male_ratio = states[:,0]/(states[:,0]+states[:,1])
plt.plot(t[1:], male_ratio, color='purple', linewidth=2)
plt.axhline(y=0.78, color='gray', linestyle=':', alpha=0.7, label='资源匮乏时雄性比例')
plt.axhline(y=0.56, color='gray', linestyle='--', alpha=0.7, label='资源充足时雄性比例')
plt.axvline(x=25, color='gray', linestyle='--', alpha=0.7)
plt.title('七鳃鳗雄性比例变化', fontsize=14, fontweight='bold')
plt.xlabel('时间')
plt.ylabel('雄性比例')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# 子图3：宿主种群
plt.subplot(2,2,3)
plt.plot(t[1:], states[:,2], color='green', linewidth=2, label='宿主种群')
plt.axvline(x=25, color='gray', linestyle='--', alpha=0.7)
plt.title('宿主种群数量', fontsize=14, fontweight='bold')
plt.xlabel('时间')
plt.ylabel('种群数量')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# 子图4：捕食者种群
plt.subplot(2,2,4)
plt.plot(t[1:], states[:,3], color='red', linewidth=2, label='捕食者种群')
plt.axvline(x=25, color='gray', linestyle='--', alpha=0.7)
plt.title('捕食者种群数量', fontsize=14, fontweight='bold')
plt.xlabel('时间')
plt.ylabel('种群数量')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ----------------------
# 4. 动态动画（展示资源切换后的连锁反应）
# ----------------------
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 50)
ax.set_ylim(0, max(np.max(states[:,0]+states[:,1]), np.max(states[:,2]), np.max(states[:,3])) * 1.1)
line_eel, = ax.plot([], [], label='七鳃鳗总数', color='blue', linewidth=2)
line_host, = ax.plot([], [], label='宿主', color='green', linewidth=2)
line_predator, = ax.plot([], [], label='捕食者', color='red', linewidth=2)
ax.axvline(x=25, color='gray', linestyle='--', alpha=0.7, label='资源切换')
ax.set_xlabel('时间', fontsize=12)
ax.set_ylabel('种群数量', fontsize=12)
ax.set_title('生态系统动态变化（资源匮乏→充足）', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

def animate(frame):
    line_eel.set_data(t[1:frame+1], states[:frame,0]+states[:frame,1])
    line_host.set_data(t[1:frame+1], states[:frame,2])
    line_predator.set_data(t[1:frame+1], states[:frame,3])
    return line_eel, line_host, line_predator

ani = FuncAnimation(fig, animate, frames=len(t)-1, interval=50, blit=True)
plt.show()

# ----------------------
# 5. 新增：资源变化对比图
# ----------------------
plt.figure(figsize=(12, 8))

# 绘制资源水平变化
plt.subplot(2,1,1)
plt.plot(t[1:], resource_levels[1:], color='orange', linewidth=3, label='资源水平')
plt.axvline(x=25, color='red', linestyle='--', alpha=0.7, label='资源切换点')
plt.title('资源水平变化 (0=匮乏, 1=充足)', fontsize=14, fontweight='bold')
plt.xlabel('时间')
plt.ylabel('资源水平')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(-0.1, 1.1)

# 绘制所有种群在同一图中的对比
plt.subplot(2,1,2)
plt.plot(t[1:], states[:,0]+states[:,1], label='七鳃鳗总数', color='blue', linewidth=2)
plt.plot(t[1:], states[:,2], label='宿主种群', color='green', linewidth=2)
plt.plot(t[1:], states[:,3], label='捕食者种群', color='red', linewidth=2)
plt.axvline(x=25, color='gray', linestyle='--', alpha=0.7, label='资源切换')
plt.title('生态系统各种群动态对比', fontsize=14, fontweight='bold')
plt.xlabel('时间')
plt.ylabel('种群数量')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()