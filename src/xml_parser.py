from typing import List
from robot.api import ExecutionResult
from dataclasses import dataclass, field

@dataclass
class TestResult:
    xml_path: str
    passed: int = field(init=False)
    failed: int = field(init=False)
    skipped: int = field(init=False)
    total: int = field(init=False)
    testcase_names: List[str] = field(init=False, default_factory=list)
    testsuite_names: List[str] = field(init=False, default_factory=list)
    testcases_status: List[str] = field(init=False, default_factory=list)
    testcases_elapsed: List[float] = field(init=False, default_factory=list)
    start_time: List[str] = field(init=False,default_factory=list)      #new
    start_date: List[str] = field(init=False,default_factory=list)      #new

    def __post_init__(self):
        result = ExecutionResult(self.xml_path)
        stats = result.statistics.total
        self.passed = stats.passed
        self.failed = stats.failed
        self.skipped = stats.skipped
        self.total = stats.total
        self.start_time = result.suite.start_time.time().replace(microsecond=0)
        self.start_date = result.suite.start_time.date()

        root_suite = result.suite
        for test in root_suite.all_tests:
            self.testcase_names.append(test.name)
            self.testsuite_names.append(test.parent.name)
            self.testcases_status.append(test.status)
            self.testcases_elapsed.append(test.elapsed_time.total_seconds())