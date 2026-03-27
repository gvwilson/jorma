"""Role name constants and method sets."""

# Sajaniemi's roles
FIXED_VALUE = "fixed value"
STEPPER = "stepper"
GATHERER = "gatherer"
MOST_RECENT = "most-recent holder"
MOST_WANTED = "most-wanted holder"
ONE_WAY_FLAG = "one-way flag"
TEMPORARY = "temporary"
ORGANIZER = "organizer"
CONTAINER = "container"

# Additional roles detectable (fully or partially) by static analysis
TOGGLE = "toggle"
LOG = "log"
LAZY_VALUE = "lazy value"

# Additional roles detectable dynamically
PHASE = "phase"  # state-machine variable
FOLLOWER = "follower"  # always holds the previous value of another variable
SNAPSHOT = "snapshot"  # point-in-time copy of another variable
GENERATOR_STATE = "generator state"  # opaque RNG / sequence state

UNKNOWN = "unknown"

# Methods that only add elements — distinguishes log from general container
_LOG_METHODS = frozenset({"append", "appendleft", "extend", "extendleft"})

# All methods that mutate a collection
CONTAINER_METHODS = frozenset(
    {
        "append",
        "appendleft",
        "add",
        "insert",
        "extend",
        "extendleft",
        "update",
        "remove",
        "discard",
        "pop",
        "popleft",
        "clear",
    }
)

# Methods that only rearrange existing elements
ORGANIZER_METHODS = frozenset({"sort", "reverse"})

# Literal values that signal "not yet computed" in lazy-value patterns.
# Note: -1 is represented in Python's AST as UnaryOp(USub, Constant(1)), not
# Constant(-1), so it is handled separately inside _is_sentinel().
_SENTINEL_CONSTANTS = frozenset({None, ""})
